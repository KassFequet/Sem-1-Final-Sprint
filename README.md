#  👵👴 Mom's Garden & Pop's Workshop – E-Commerce Web Application
 
A fully functional e-commerce website built as part of a second-semester Software Development project. The application simulates an online store for a local hardware shop owned by an elderly couple, complete with dynamic routing, mock API integration, cart functionality, and component testing.
 
## 🚀 Tech Stack
 
- ⚛️ React + Vite (Frontend Framework & Bundler)
- 📄 JSON Server (Mock Backend API)
- 🧪 Vitest (Unit Testing Framework)
- 🔁 React Router (SPA routing, no page reloads)
- 🎨 CSS Modules
 
---
 
## 📁 Project Structure
 
src/
├── components/     # Reusable UI components (e.g. ProductCard, CartItem)
├── pages/          # Main routed views (e.g. Home, About, Products, Checkout)
├── context/        # React Context (Cart Context)
├── tests/          # Unit tests using Vitest
├── App.jsx         # Main app logic and route definitions
├── main.jsx        # App entry point
public/
db.json             # Mock data for products and cart
 
---
 
## 🛠 Features
 
-  **Product Listing Page**  
  Displays items fetched from a mock API with images, pricing, and descriptions.
 
-  **Product Detail View**  
  Expandable or routed view to see individual item details (if implemented).
 
-  **Shopping Cart**  
  Add/remove items, quantity management, and total price calculation.
 
-  **Checkout Page**  
  Summary of items and mock payment confirmation.
 
-  **Routing**  
  SPA navigation using React Router (no full-page reloads).
 
-  **Component Testing**  
  Minimum of 3 core components tested using Vitest.
 
---
 
## 🔗 Live Preview
 
👉 [Live Demo](https://www.figma.com/proto/hlGbBnLK6zS4mjWAkJhth4/Final-Sprint-Mom-s-Garden---Pop-s-Workshop?node-id=0-1&t=jAjIqvTBBeKKMgRB-1)
 
---
 
## 🧪 Testing with Vitest
 <!--
 
 ```bash
Run all tests
npm run test  
 
-->
 
This project was created for educational purposes and is not intended for commercial use.
 
## Acknowledgements
 
Instructor: Levin (UI/UX Design Principles)
 
Instructor: Noman (Javascript and React)
 
Instructor: Dr. Malik (Javascript Review)
