<template>
  <div class="container">
    <div class="login-box">
      <h1 class="logo">Hey<span>#</span></h1>

      <form @submit.prevent="login">
        <div class="input-group">
          <label for="email">E-mail</label>
          <div class="input-wrapper">
            <input id="email" type="email" v-model="email" placeholder="Digite seu e-mail" required />
            <span class="icon">📧</span>
          </div>
          <p v-if="errors.email" class="error-message">{{ errors.email }}</p>
        </div>

        <div class="input-group">
          <label for="password">Senha</label>
          <div class="input-wrapper">
            <input id="password" type="password" v-model="password" placeholder="Digite sua senha" required />
            <span class="icon">🔒</span>
          </div>
          <p v-if="errors.password" class="error-message">{{ errors.password }}</p>
        </div>

        <button class="btn" type="submit">ENTRAR</button>

        <p v-if="errors.general" class="error-message">{{ errors.general }}</p>
      </form>

      <div class="links">
        <router-link to="/register">Criar conta</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
      errors: {}, // Armazena os erros da API
    };
  },
  methods: {
    async login() {
      this.errors = {}; // Limpa os erros antes de enviar a requisição

      try {
        const response = await axios.post("http://localhost:8000/api/login/", {
          email: this.email,
          password: this.password,
        });

        console.log("Login bem-sucedido:", response.data);
        this.$router.push("/sucess"); // Redireciona para a tela de menu
      } catch (error) {
        if (error.response && error.response.data) {
          this.errors = error.response.data; // Captura os erros da API
        } else {
          this.errors.general = "Erro ao conectar ao servidor.";
        }
      }
    },
  },
};
</script>

<style scoped>
/* Fundo */
.container {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: url("https://source.unsplash.com/1600x900/?office,laptop") no-repeat center center/cover;
}

/* Caixa de login */
.login-box {
  background: rgba(255, 255, 255, 0.9);
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
  width: 350px;
}

/* Logo */
.logo {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.logo span {
  color: #ffcc00;
}

/* Inputs */
.input-group {
  margin-bottom: 15px;
  text-align: left;
}

.input-group label {
  font-size: 14px;
  font-weight: bold;
  color: #444;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-wrapper input {
  width: 100%;
  padding: 10px 40px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 14px;
}

.icon {
  position: absolute;
  left: 10px;
  color: #777;
}

/* Botão */
.btn {
  background: #333;
  color: white;
  border: none;
  padding: 12px;
  width: 100%;
  font-size: 14px;
  border-radius: 5px;
  cursor: pointer;
  transition: 0.3s;
}

.btn:hover {
  background: #000;
}

/* Mensagem de erro */
.error-message {
  color: red;
  font-size: 12px;
  margin-top: 5px;
}
</style>
