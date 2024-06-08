<template>
  <div class="container">
    <div class="card"  style="border-radius: 2rem;">
      <div class="card-header">
        <h4 class="headline">Employees</h4>
      </div>
      <div class="card-body">
        <table class="data-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Email</th>
              <th>Role</th>
              <th>Remove User</th>
              <th>Change Password</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(employee, index) in employees" :key="employee.id">
              <td>{{ index + 1 }}</td>
              <td>{{ employee.username }}</td>
              <td>{{ employee.email }}</td>
              <td>{{ employee.role }}</td>
              <td>
                <button v-if="employee.username!=currentUser.username" @click="removeUser(employee.id)" class="btn delete-btn icon-btn">
                  <i class="fas fa-trash"></i> Remove
                </button>
              </td>
              <td>
                <button @click="showChangePasswordModalF(employee.username)" class="btn icon-btn">
                  <i class="fas fa-key"></i> Change Password
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-if="showChangePasswordModal" class="modal is-active">
      <div class="modal-background" @click="closeModal"></div>
      <div class="modal-card">
        <header class="modal-card-head">
          <p class="modal-card-title"><strong>Change Password for {{ selectedUser.username }}</strong></p>
          <button class="delete" aria-label="close" @click="closeModal"></button>
        </header>
        <section class="modal-card-body">
          <form @submit.prevent="changePassword">
            <div class="field">
              <label class="label">Current Password</label>
              <div class="control">
                <input v-model="currentPassword" type="password" class="input" placeholder="Current Password" required>
              </div>
            </div>
            <div class="field">
              <label class="label">New Password</label>
              <div class="control">
                <input v-model="newPassword" type="password" class="input" placeholder="New Password" required>
              </div>
            </div>
            <div class="field">
              <label class="label">Confirm New Password</label>
              <div class="control">
                <input v-model="confirmPassword" type="password" class="input" placeholder="Confirm New Password" required>
              </div>
            </div>
          </form>
        </section>
        <footer class="modal-card-foot">
          <button class="button is-primary" @click="changePassword">Change Password</button>
          <button class="button" @click="closeModal">Cancel</button>
        </footer>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import store from '@/store';
import { toast } from 'bulma-toast';

export default {
  name: 'EmployeesView',
  data() {
    return {
      headers: [
        { text: '#', value: 'index' },
        { text: 'Name', value: 'username' },
        { text: 'Email', value: 'email' },
        { text: 'Role', value: 'role' },
        { text: 'Remove User', value: 'actions', sortable: false },
        { text: 'Change Password', value: 'actions', sortable: false },
      ],
      employees: [],
      currentUser: null,
      showChangePasswordModal: false,
      selectedUser: {},
      currentPassword: '',
      newPassword: '',
      confirmPassword: '',
      valid: false,
    };
  },
  mounted() {
    this.getEmployees();
  },
  methods: {
    async getEmployees() {
      await axios
        .get('/accounts/employees/', {
          headers: {
            Authorization: `Bearer ${store.state.token}`
          },
        })
        .then(response => {
        this.employees = response.data;
        this.currentUser = this.employees.find(employee => employee.username === store.state.username);
        })
        .catch(error => {
          console.error('Error fetching employees:', error);
        });
    },
    showChangePasswordModalF(username) {
      console.log(username,"ok");
      const user = this.employees.find(employee => employee.username === username);
      if (this.currentUser.role === 'ADMIN' && user) {
        console.log(user.username,"ok");
        this.selectedUser = user;
        this.currentPassword = '';
        this.newPassword = '';
        this.confirmPassword = '';
        this.showChangePasswordModal = true;
      }
    },
    removeUser(userId) {
      if (confirm('Are you sure you want to remove this user?')) {
        axios
          .delete(`/accounts/employees/${userId}/delete/`,{
          headers: {
            Authorization: `Bearer ${store.state.token}`
            },
          })
          .then(() => {
            const index = this.employees.findIndex(employee => employee.id === userId);
            if (index > -1) {
              this.employees.splice(index, 1);
              toast({ message: 'User deleted successfully', type: 'is-success' });
            }
          })
          .catch(error => {
            console.error('Error removing user:', error);
            toast({ message: 'Error deleting user', type: 'is-danger' });
          });
      }
    },
    closeModal() {this.showChangePasswordModal = false},
    changePassword() {
      this.valid = true;

      if (this.currentPassword === '' || this.newPassword === '' || this.confirmPassword !== this.newPassword) {
        this.valid = false;
      }

      if (this.valid) {
        axios
          .post(`/accounts/change/${this.selectedUser.id}/password/`, {
            old_password: this.currentPassword,
            new_password1: this.newPassword,
            new_password2: this.confirmPassword,
          }, {
              headers: {
                Authorization: `Bearer ${store.state.token}`
              }
            })
          .then(() => {
            toast({ message: 'Password changed successfully', type: 'is-success' });
            this.showChangePasswordModal = false;
            this.currentPassword = '';
            this.newPassword = '';
            this.confirmPassword = '';
            console.log('Password changed successfully');
          })
          .catch(error => {
            const errorsMessage = error.response.data.errors;
            const errorMessageString = JSON.stringify(errorsMessage); // Convert the errors to a string
            toast({
              message: `The Error is: ${errorMessageString}.`,
              type: 'is-danger',
              duration: 5000,
            });
            console.error('Error changing password:', error);
          });
      }
    },
  },
};
</script>

<style scoped>
.app {
  font-family: var(--font-family);
  background-color: var(--black-background-color);
  color: var(--text-color);
  padding: 20px;
}

.container {
  margin-top: 20px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50px; /* add border radius for round corners */
}

.card {
  background-color: var(--black-background-color);
  border: 1px solid var(--border-color);
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-header {
  background-color: var(--menu-background-color);
  padding: 10px 15px;
  border-bottom: 1px solid var(--border-color);
}

.headline {
  margin: 0;
  color: var(--text-color-titles);
}

.card-body {
  padding: 15px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
}

.data-table th, .data-table td {
  border: 1px solid var(--border-color);
  padding: 8px;
  color: var(--text-color);
}

.data-table th {
  background-color: var(--menu-background-color);
  text-align: left;
}

.btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-color);
  padding-left: 40%;  /* Adjust button padding */
}
.btn i {
  margin-right: 5px;  /* Add space between icon and text */
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  color: var(--primary-color);
}

.delete-btn {
  color: red;
  padding-left: 40%;  /* Adjust button padding */
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background: var(--menu-background-color);
  padding: 20px;
  border-radius: 4px;
  width: 500px;
  max-width: 100%;
}

.close {
  float: right;
  font-size: 24px;
  cursor: pointer;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
  background-color: var(--white-background-color);
  border: 1px solid var(--border-color);
  border-radius: 4px;
  color: var(--text-black-color);
}

.form-control:focus {
  outline: none;
  border-color: var(--primary-color);
}

.form-label {
  margin-bottom: 5px;
  font-weight: bold;
  color: var(--text-black-color);
}

.table {
  width: 100%;
  border-collapse: collapse;
}

.table th, .table td {
  padding: 12px;
  border: 1px solid var(--border-color);
  text-align: left;
}

.table th {
  background-color: var(--menu-background-color);
  color: var(--text-color);
}

.table tr:nth-child(even) {
  background-color: var(--white-background-color);
}

.table tr:nth-child(odd) {
  background-color: var(--background-color);
}

.table tbody tr:hover {
  background-color: var(--primary-color);
  color: var(--text-color);
}

.alert {
  padding: 20px;
  background-color: var(--primary-color);
  color: var(--text-color);
  margin-bottom: 15px;
  border-radius: 4px;
}

.alert .close {
  margin-left: 15px;
  color: var(--text-color);
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.alert .close:hover {
  color: var(--text-color-secondary);
}
</style>
