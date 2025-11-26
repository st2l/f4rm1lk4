<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script>
export default {
  computed: {
    layout() {
      return this.$route.meta.layout || "base-layout";
    },
  },
};
</script>

<style lang="scss">
:root {
  --terminal-bg: #050805;
  --terminal-panel: #0c1f11;
  --terminal-panel-hover: #173c22;
  --terminal-border: #33ff66;
  --terminal-border-muted: rgba(51, 255, 102, 0.35);
  --terminal-text: #fefefe;
  --terminal-text-strong: #d4ffd4;
  --terminal-muted: #7ed38f;
}

html,
body,
#app {
  height: 100%;
  margin: 0;
  background-color: var(--terminal-bg);
  color: var(--terminal-text);
}

body {
  font-family: "Source Code Pro", monospace !important;
  text-shadow: 0 0 6px rgba(51, 255, 138, 0.28);
  line-height: 1.55;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    transparent 0 2px,
    rgba(12, 38, 14, 0.3) 2px 4px
  );
  opacity: 0.25;
  mix-blend-mode: soft-light;
  z-index: 10;
}

.text-cbs {
  color: var(--terminal-text) !important;
}

.bg-cbs {
  background: radial-gradient(circle at 20% 20%, #0e2611, #030904) !important;
  border-bottom: 1px solid var(--terminal-border);
}

.terminal-layout,
.q-page-container,
.q-page {
  background: radial-gradient(circle at top, rgba(24, 79, 37, 0.3), transparent)
      no-repeat,
    var(--terminal-bg);
  color: var(--terminal-text);
}

.q-page-container {
  padding-bottom: 32px;
}

.terminal-header,
.terminal-toolbar,
.terminal-tabs {
  background: transparent;
  color: var(--terminal-text);
}

.terminal-tabs .q-route-tab {
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.q-card,
.q-table__container {
  background: rgba(6, 24, 12, 0.92) !important;
  border: 1px solid var(--terminal-border);
  box-shadow: 0 0 24px rgba(51, 255, 138, 0.2);
}

.q-card__section,
.q-card__actions {
  background: transparent !important;
  color: var(--terminal-text);
}

.q-table thead tr,
.q-table tbody tr {
  background: rgba(5, 18, 10, 0.92) !important;
}

.q-table th,
.q-table td {
  border-color: var(--terminal-border-muted) !important;
  color: var(--terminal-text);
  background: transparent;
}

.q-table__top,
.q-table__bottom {
  background: rgba(5, 25, 12, 0.95);
  border-top: 1px solid var(--terminal-border-muted);
}

.q-field__control {
  background: rgba(7, 34, 17, 0.65);
  border: 1px solid var(--terminal-border-muted);
}

.q-field--outlined .q-field__control:before,
.q-field--outlined .q-field__control:after {
  border: none;
}

.q-field__label,
.q-field__native,
.q-field__marginal,
.q-field__bottom {
  color: var(--terminal-muted);
}

.q-field__native {
  color: var(--terminal-text);
}

.q-btn.bg-cbs,
.q-btn.text-cbs,
.q-btn.bg-primary {
  background: transparent !important;
  border: 1px solid var(--terminal-border);
  color: var(--terminal-text) !important;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  box-shadow: 0 0 14px rgba(51, 255, 138, 0.4);
}

.q-btn.bg-cbs:hover,
.q-btn.bg-primary:hover {
  background: var(--terminal-panel-hover) !important;
}

.q-input input,
.q-select__content {
  caret-color: var(--terminal-text);
}

a,
.text-primary {
  color: var(--terminal-text-strong);
}

.q-avatar img {
  filter: hue-rotate(90deg) saturate(1.4);
}

.q-page .text-h6,
.q-card__section .text-h6 {
  color: var(--terminal-text-strong);
}

.q-table__title,
.q-table__bottom-item {
  color: var(--terminal-text);
}
</style>
