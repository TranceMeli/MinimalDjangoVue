<template>
  <nav>
    <div class="nav-inner">
      <div class="nav-logo">DjangoVue</div>
      <ul class="nav-links">
        <li v-for="link in links" :key="link.label">
          <a
            href="#"
            :class="{ active: active === link.label }"
            @click.prevent="navigate(link)"
          >
            {{ link.label }}
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const active = ref('Home')

const links = [
  { label: 'Home',     endpoint: 'home' },
  { label: 'About',    endpoint: 'about' },
  { label: 'Projects', endpoint: 'projects' },
  { label: 'Contact',  endpoint: 'contact' },
]

const emit = defineEmits(['navigate'])

function navigate(link) {
  active.value = link.label
  emit('navigate', link.endpoint)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500&display=swap');

nav {
  position: sticky;
  top: 0;
  background: #fafaf8;
  border-bottom: 1px solid #e8e6e0;
  z-index: 100;
  font-family: 'DM Sans', sans-serif;
}

.nav-inner {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.nav-logo {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #1a1a1a;
  cursor: pointer;
  
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 2px;
  list-style: none;
}

.nav-links a {
  display: block;
  padding: 6px 14px;
  font-size: 14px;
  color: #555;
  text-decoration: none;
  border-radius: 6px;
  transition: background .15s, color .15s;
}

.nav-links a:hover {
  background: #eeede9;
  color: #1a1a1a;
}

.nav-links a.active {
  color: #1a1a1a;
  font-weight: 500;
  background: #e8e6e0;
}
</style>