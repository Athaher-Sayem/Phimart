// Frontend-only illustrative data. No requests are made to the application API.
const routes = {
  products: {
    method: 'GET', path: '/api/v1/products/', caption: 'Product fields from ProductSerializer',
    response: { id: 12, name: 'Example product', description: 'Illustrative item', price: '24.00', stock: 18, category: 3, price_with_tax: 26.4, images: [] }
  },
  categories: {
    method: 'GET', path: '/api/v1/categories/', caption: 'Category fields from CategorySerializer',
    response: { id: 3, name: 'Example category', description: 'Illustrative category', product_count: 1 }
  },
  carts: {
    method: 'POST', path: '/api/v1/carts/', caption: 'Cart route · authentication required · example only',
    response: { note: 'Conceptual response: no request is sent.', authentication: 'required', nested_route: '/api/v1/carts/{id}/items/' }
  },
  orders: {
    method: 'POST', path: '/api/v1/orders/', caption: 'Order route · authentication required · example only',
    response: { note: 'Conceptual response: no order is created.', authentication: 'required', action: '/api/v1/orders/{id}/cancel/' }
  }
};
const output = document.getElementById('route-json');
const buttons = document.querySelectorAll('[data-route]');
function selectRoute(key) {
  const route = routes[key];
  if (!route) return;
  document.getElementById('route-method').textContent = route.method;
  document.getElementById('route-path').textContent = route.path;
  document.getElementById('route-caption').textContent = route.caption;
  output.textContent = JSON.stringify(route.response, null, 2);
  buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.route === key)));
}
buttons.forEach(button => button.addEventListener('click', () => selectRoute(button.dataset.route)));
selectRoute('products');
document.getElementById('copy-route').addEventListener('click', async event => {
  const button = event.currentTarget;
  try {
    await navigator.clipboard.writeText(output.textContent);
    button.textContent = 'COPIED';
  } catch {
    button.textContent = 'COPY UNAVAILABLE';
  }
  setTimeout(() => { button.textContent = 'COPY JSON'; }, 2200);
});
