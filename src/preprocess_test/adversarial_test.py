def classifier_graph(self):
    """Constructs classifier graph from inputs to classifier loss.
    * Caches the VatxtInput object in `self.cl_inputs`
    * Caches tensors: `cl_embedded`, `cl_logits`, `cl_loss`
    Returns:
      loss: scalar float.
    """
    inputs = _inputs('train', pretrain=False)
    self.cl_inputs = inputs
    embedded = self.layers['embedding'](inputs.tokens)
    self.tensors['cl_embedded'] = embedded

    _, next_state, logits, loss = self.cl_loss_from_embedding(
        embedded, return_intermediates=True)
    tf.summary.scalar('classification_loss', loss)
    self.tensors['cl_logits'] = logits
    self.tensors['cl_loss'] = loss

    if FLAGS.single_label:
      indices = tf.stack([tf.range(FLAGS.batch_size), inputs.length - 1], 1)
      labels = tf.expand_dims(tf.gather_nd(inputs.labels, indices), 1)
      weights = tf.expand_dims(tf.gather_nd(inputs.weights, indices), 1)
    else:
      labels = inputs.labels
      weights = inputs.weights
    acc = layers_lib.accuracy(logits, labels, weights)
    tf.summary.scalar('accuracy', acc)

    adv_loss = (self.adversarial_loss() * tf.constant(
        FLAGS.adv_reg_coeff, name='adv_reg_coeff'))
    tf.summary.scalar('adversarial_loss', adv_loss)

    total_loss = loss + adv_loss

    with tf.control_dependencies([inputs.save_state(next_state)]):
      total_loss = tf.identity(total_loss)
      tf.summary.scalar('total_classification_loss', total_loss)
    return total_loss


def adversarial_loss(embedded, loss, loss_fn):
  """Adds gradient to embedding and recomputes classification loss."""
  grad, = tf.gradients(
      loss,
      embedded,
      aggregation_method=tf.AggregationMethod.EXPERIMENTAL_ACCUMULATE_N)
  grad = tf.stop_gradient(grad)
  perturb = _scale_l2(grad, FLAGS.perturb_norm_length)
  return loss_fn(embedded + perturb)


def _scale_l2(x, norm_length):
  # shape(x) = (batch, num_timesteps, d)
  # Divide x by max(abs(x)) for a numerically stable L2 norm.
  # 2norm(x) = a * 2norm(x/a)
  # Scale over the full sequence, dims (1, 2)
  alpha = tf.reduce_max(tf.abs(x), (1, 2), keep_dims=True) + 1e-12
  l2_norm = alpha * tf.sqrt(
      tf.reduce_sum(tf.pow(x / alpha, 2), (1, 2), keep_dims=True) + 1e-6)
  x_unit = x / l2_norm
  return norm_length * x_unit


def adversarial_loss(self):
    """Compute adversarial loss based on FLAGS.adv_training_method."""

    def random_perturbation_loss():
      return adv_lib.random_perturbation_loss(self.tensors['cl_embedded'],
                                              self.cl_inputs.length,
                                              self.cl_loss_from_embedding)

    def adversarial_loss():
      return adv_lib.adversarial_loss(self.tensors['cl_embedded'],
                                      self.tensors['cl_loss'],
                                      self.cl_loss_from_embedding)
