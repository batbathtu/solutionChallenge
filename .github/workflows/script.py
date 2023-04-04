const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = process.env.PORT || 5000;

// Database connection
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/ecosync', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Middleware
app.use(bodyParser.json());
app.use(cors());

// Models
const User = mongoose.model('User', {
  name: String,
  email: String,
  password: String,
  sustainabilityGoals: [{
    category: String,
    target: Number,
    progress: Number,
  }],
  habits: [{
    category: String,
    description: String,
    currentValue: Number,
    targetValue: Number,
  }],
});

// Routes
app.get('/users', async (req, res) => {
  const users = await User.find({});
  res.json(users);
});

app.post('/users', async (req, res) => {
  const newUser = new User(req.body);
  await newUser.save();
  res.json(newUser);
});

app.get('/users/:id', async (req, res) => {
  const user = await User.findById(req.params.id);
  res.json(user);
});

app.patch('/users/:id', async (req, res) => {
  const updatedUser = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
  res.json(updatedUser);
});

app.delete('/users/:id', async (req, res) => {
  await User.findByIdAndDelete(req.params.id);
  res.json({ message: 'User deleted' });
});

// Start server
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
