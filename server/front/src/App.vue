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
  --terminal-bg: #020c02;
  --terminal-panel: #061307;
  --terminal-panel-hover: #0f3011;
  --terminal-border: #32ff74;
  --terminal-border-muted: rgba(50, 255, 116, 0.3);
  --terminal-text: #c2ffc3;
  --terminal-text-strong: #74ff5e;
  --terminal-muted: #6dcf69;
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
  text-shadow: 0 0 6px rgba(55, 255, 125, 0.22);
  line-height: 1.55;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    transparent 0 2px,
    rgba(0, 0, 0, 0.22) 2px 4px
  );
  opacity: 0.25;
  mix-blend-mode: soft-light;
  z-index: 10;
}

.text-cbs {
  color: var(--terminal-text) !important;
}

.bg-cbs {
  background: radial-gradient(circle at 20% 20%, #0c2b0f, #010a03) !important;
  border-bottom: 1px solid var(--terminal-border);
}

.terminal-layout,
.q-page-container,
.q-page {
  background: radial-gradient(circle at top, rgba(8, 35, 8, 0.45), transparent)
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
  background: rgba(2, 14, 6, 0.9);
  border: 1px solid var(--terminal-border);
  box-shadow: 0 0 24px rgba(40, 255, 122, 0.15);
}

.q-table thead tr,
.q-table tbody tr {
  background: transparent !important;
}

.q-table th,
.q-table td {
  border-color: var(--terminal-border-muted) !important;
  color: var(--terminal-text);
}

.q-table__top,
.q-table__bottom {
  background: rgba(2, 14, 6, 0.95);
  border-top: 1px solid var(--terminal-border-muted);
}

.q-field__control {
  background: rgba(0, 0, 0, 0.4);
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
  box-shadow: 0 0 14px rgba(61, 255, 131, 0.35);
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
