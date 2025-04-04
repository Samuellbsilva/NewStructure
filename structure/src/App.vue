<template>
  <div class="flex flex-col justify-center items-center h-screen">
    <p class="text-2xl font-bold mb-0">{{ mensagem }}</p>
    <button @click="fetchMensagem" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-2 rounded-full mb-1 mt-2">Carregar Mensagem</button>
    <button @click="reiniciarMensagem" class="bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-full text-sm py-1 px-2">Reiniciar Mensagem</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mensagem: "Clique para carregar a mensagem...",
    };
  },
  methods: {
    async fetchMensagem() {
      try {
        const response = await fetch("http://127.0.0.1:5000/mensagem", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ nome: "Samuel" }),
        });

        if (!response.ok) {
          throw new Error("Erro ao buscar a mensagem");
        }

        const data = await response.json();
        this.mensagem = data.mensagem;
      } catch (error) {
        console.error("Erro:", error);
        this.mensagem = "Erro ao carregar mensagem";
      }
    },
    reiniciarMensagem() {
      this.mensagem = "Clique para carregar a mensagem...";
    }
  }
};
</script>
