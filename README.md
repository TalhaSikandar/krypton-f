# **Krypton - Streamlined Supply Chain Management**

## **Introduction**

Welcome to **Krypton**, your one-stop solution for streamlined supply chain management! This web-based platform empowers businesses of all sizes to centralize and optimize their operations. Krypton fosters better communication, data visibility, and control, ultimately helping you achieve a competitive edge.

## **Tech Stack**

### **Backend:**
- **Django** (Python) with Django REST Framework (robust APIs) (Aizaz + Talha)

### **Database:**
- **SQLITE** (for initial development) (Aizaz + Talha)

### **Frontend:**
- **Vue.js** (dynamic and user-friendly interface) (Izza + Ayesha)

### **Frontend Dependencies:**
- **Vue** (requires Node.js)
- **Bulma** (styling framework)
- **Bulma Toast** (notifications)
- **Vue Chart.js** (data visualization)

### **Authentication:**
- **Simple JWT** (optional, replace if needed)

## **Functionality Overview**

### **User Management:**
- **Company Signup/Login:** Create and manage company accounts.
- **Admin Signup/Login/Password Change:** Manage administrative access within a company.
- **Manager Signup/Login/Password Change:** Manage manager access within a company, limited to store-related functions.

### **Company Management (Admin:Izza):**
- View, edit, and delete company information.
- Manage all aspects of the company's supply chain.

### **Store Management (Admin/Manager:Talha):**
- Add, edit, and delete stores.
- Visualize data: Sales trends, warehouse inventory, and product availability.

### **Warehouse Management (Admin:Ayesha):**
- Add, edit, and delete warehouses.
- Track current product levels across warehouses.

### **Product Management (Admin:Ayesha):**
- Add, edit, and delete products.
- Associate products with required raw materials and quantities.
- Track product availability in warehouses.

### **Inventory Management (Admin:Talha):**
- Add raw materials (suppliers and costs).
- Manage and track raw material inventory.

### **Supplier Management (Admin:Aizaz):**
- Add, edit, and delete suppliers.
- Manage supplier information and raw material costs.

### **Stock Management:**
- Automatically deduct products from warehouses when adding them to stores.
- Maintain accurate inventory levels.

### **Additional Features:**
- Session maintenance (Talha)
- Minimalistic user interface
- Bulk company deletion (highly recommended with safeguards, consider archival instead) (Aizaz)

## **Getting Started (Backend Setup):**
1. Install required dependencies using `pip install -r requirements.txt` commands.
2. Configure Django settings and database connection.
3. Set up Simple JWT authentication (optional, explore alternatives if needed).

## **Getting Started (Frontend Setup):**
1. Install Vue CLI and `vue create` your frontend project.
2. Install Vue, Bulma, Bulma Toast, and Vue Chart.js.
3. Integrate your frontend with the backend APIs.

## **Deployment:**
- Haven't Done it yet but after finalizing everything.

## **Contributing**

We do not welcome contributions to Krypton!

## **Team Members:**
- Rao Muhammad Talha - 050
- Ayesha Siddiqa - 106
- Aizaz Amin - 056
- Izza Arooj - 006

## **Disclaimer:**

This `README.md` provides a high-level overview. For detailed implementation instructions, refer to the project's codebase.
