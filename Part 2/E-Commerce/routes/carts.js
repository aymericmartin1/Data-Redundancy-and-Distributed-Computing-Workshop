const express = require("express");
const Cart = require("../models/Cart");
const Product = require("../models/Product");
const { v4: uuidv4 } = require("uuid");

const router = express.Router();

router.post("/:userId", async (req, res) => {
    try {
      const { items } = req.body;
  
      // Validate the cart items
      if (!items || !Array.isArray(items) || items.length === 0) {
        return res.status(400).json({ error: "Invalid cart items" });
      }
  
      let totalPrice = 0;
  
      // Calculate total price
      for (const item of items) {
        const product = await Product.findById(item.productId);
        if (!product) {
          return res.status(404).json({ error: `Product not found: ${item.productId}` });
        }
        totalPrice += product.price * item.quantity;
      }
  
      // Create a new cart
      const newCart = new Cart({
        _id: uuidv4(),
        userId: req.params.userId,
        items,
        totalPrice
      });
  
      await newCart.save();
      res.status(201).json(newCart);
    } catch (err) {
      res.status(500).json({ error: "Server error" });
    }
  });
  

  router.get("/:userId", async (req, res) => {
    try {
      const cart = await Cart.findOne({ userId: req.params.userId });
      if (!cart) {
        return res.status(404).json({ error: "Cart not found for this user" });
      }
      res.json(cart);
    } catch (err) {
      res.status(500).json({ error: "Server error" });
    }
  });
  
  router.delete("/:userId", async (req, res) => {
    try {
      const deletedCart = await Cart.findOneAndDelete({ userId: req.params.userId });
      if (!deletedCart) {
        return res.status(404).json({ error: "Cart not found for this user" });
      }
  
      res.json({ message: "Cart deleted successfully" });
    } catch (err) {
      res.status(500).json({ error: "Server error" });
    }
  });
  
  module.exports = router;