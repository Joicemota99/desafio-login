<template>
    <div class="success-container">
      <div class="success-box">
        <h2>🎉 Login realizado com sucesso! 🎉</h2>
        <p>Redirecionando para o menu...</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    mounted() {
      setTimeout(() => {
        this.$router.push("/menu"); // Redireciona para a tela de menu após 3 segundos
      }, 3000);
    },
  };
  </script>
  
  <style scoped>
  .success-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background: #f0f8ff;
  }
  
  .success-box {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    text-align: center;
    max-width: 400px;
  }
  
  h2 {
    color: #2d8cf0;
  }
  
  p {
    color: #333;
    font-size: 16px;
  }
  </style>
  