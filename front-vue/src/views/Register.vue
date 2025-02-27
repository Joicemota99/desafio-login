<template>
  <div class="container">
    <div class="register-box">
      <h1 class="logo">Hey<span>#</span></h1>

      <div class="input-group">
        <label for="nome">Nome</label>
        <div class="input-wrapper">
          <input v-model="nome" id="nome" type="text" placeholder="Digite seu nome" />
          <span class="icon">📝</span>
        </div>
        <p v-if="errors.nome" class="error-message">{{ errors.nome }}</p>
      </div>

      <div class="input-group">
        <label for="email">E-mail</label>
        <div class="input-wrapper">
          <input v-model="email" id="email" type="email" placeholder="Digite seu e-mail" />
          <span class="icon">📧</span>
        </div>
        <p v-if="errors.email" class="error-message">{{ errors.email }}</p>
      </div>

      <div class="input-group">
        <label for="senha">Senha</label>
        <div class="input-wrapper">
          <input
            v-model="password"
            id="senha"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Crie uma senha"
          />
          <span class="icon" @click="togglePassword">👁️</span>
        </div>
        <p v-if="errors.password" class="error-message">{{ errors.password }}</p>
      </div>

      <div class="input-group">
        <label for="confirmarSenha">Confirmar Senha</label>
        <div class="input-wrapper">
          <input
            v-model="confirmPassword"
            id="confirmarSenha"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Confirme sua senha"
          />
          <span class="icon" @click="togglePassword">👁️</span>
        </div>
        <p v-if="errors.confirmPassword" class="error-message">{{ errors.confirmPassword }}</p>
      </div>

      <button class="btn" @click="register">CRIAR CONTA</button>
      <button class="btn cancel" @click="$router.push('/')">CANCELAR</button>

      <div class="links">
        <a href="#" @click.prevent="$router.push('/')">Já tem uma conta? Faça login</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      nome: "",
      email: "",
      password: "",
      confirmPassword: "",
      showPassword: false,
      errors: {},
    };
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
    },
    validateForm() {
      this.errors = {};

      // Validação do nome (apenas letras e não vazio)
      if (!this.nome.trim()) {
        this.errors.nome = "O nome é obrigatório.";
      } else if (!/^[a-zA-ZÀ-ÿ\s]+$/.test(this.nome)) {
        this.errors.nome = "O nome deve conter apenas letras.";
      }

      // Validação do e-mail
      if (!this.email.trim()) {
        this.errors.email = "O e-mail é obrigatório.";
      } else if (!/^\S+@\S+\.\S+$/.test(this.email)) {
        this.errors.email = "E-mail inválido.";
      }

      // Validação da senha
      if (!this.password) {
        this.errors.password = "A senha é obrigatória.";
      } else if (this.password.length < 8) {
        this.errors.password = "A senha deve ter pelo menos 8 caracteres.";
      } else if (!/[A-Z]/.test(this.password)) {
        this.errors.password = "A senha deve ter pelo menos uma letra maiúscula.";
      } else if (!/[0-9]/.test(this.password)) {
        this.errors.password = "A senha deve ter pelo menos um número.";
      } else if (!/[\W_]/.test(this.password)) {
        this.errors.password = "A senha deve ter pelo menos um caractere especial.";
      }

      // Validação da confirmação de senha
      if (this.confirmPassword !== this.password) {
        this.errors.confirmPassword = "As senhas não coincidem.";
      }

      return Object.keys(this.errors).length === 0;
    },
    async register() {
      if (!this.validateForm()) return;

      try {
        const response = await axios.post("http://localhost:8000/api/register/", {
          nome: this.nome,
          email: this.email,
          password: this.password,
        });

        console.log("Registro bem-sucedido:", response.data);
        this.$router.push("/menu"); // Redireciona para a tela de menu
      } catch (error) {
        console.error("Erro ao registrar:", error);
        alert("Erro ao registrar. Verifique os dados e tente novamente.");
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
  background: url("https://source.unsplash.com/1600x900/?technology,abstract") no-repeat center center/cover;
}

/* Caixa de cadastro */
.register-box {
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
  right: 10px;
  cursor: pointer;
}

/* Mensagens de erro */
.error-message {
  color: red;
  font-size: 12px;
  margin-top: 5px;
}

/* Botões */
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

.btn.cancel {
  background: #ccc;
  color: #333;
  margin-top: 10px;
}

.btn.cancel:hover {
  background: #bbb;
}

/* Links */
.links {
  margin-top: 15px;
  font-size: 14px;
}

.links a {
  color: #333;
  text-decoration: none;
  font-weight: bold;
}

.links a:hover {
  text-decoration: underline;
}
</style>
