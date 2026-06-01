<template>
  <div>
    <NavBar @navigate="fetchMessage" />
    <main>
      <p v-if="message">{{ message }}</p>
      <p v-if="error" style="color: red">{{ error }}</p>
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import NavBar from './components/NavBar.vue'

const message = ref('')
const error = ref('')

async function fetchMessage(endpoint) {
  try {
    const res = await axios.get(`http://localhost:8000/api/${endpoint}/`)
    message.value = res.data.message
    error.value = ''
  } catch (e) {
    error.value = 'Error: Backend not running?'
  }
}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}
</style>