def fgsm(model, x, y, epsilon: float, loss_fn):
    """Return an FGSM-perturbed input for evaluation; this is not a defense."""
    import torch
    if epsilon < 0: raise ValueError('epsilon must be non-negative')
    x_adv=x.detach().clone().requires_grad_(True)
    loss=loss_fn(model(x_adv),y); model.zero_grad(set_to_none=True); loss.backward()
    return (x_adv + epsilon*x_adv.grad.sign()).detach()
