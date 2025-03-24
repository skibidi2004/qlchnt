import axios from "@/axios"; // Import axios có chứa token

export const getCart = () => axios.get("/api/cart/");
export const addToCart = (productId, quantity = 1) => 
    axios.post("/api/cart/items/", { product: productId, quantity });
export const removeFromCart = (cartItemId) => 
    axios.delete(`/api/cart/items/${cartItemId}/`);
export const checkout = () => axios.post("/api/orders/checkout/");
