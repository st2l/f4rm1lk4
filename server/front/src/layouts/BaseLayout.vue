<template>
  <q-layout class="terminal-layout" view="hHh lpR fFf">
    <q-header elevated class="terminal-header bg-cbs text-cbs">
      <q-toolbar class="terminal-toolbar bg-cbs text-cbs">
        <q-avatar>
          <img src="@/assets/cat.png" />
        </q-avatar>
        <q-toolbar-title> f4rm1lk4 </q-toolbar-title>
        <q-tabs class="terminal-tabs bg-cbs text-cbs" shrink>
          <q-route-tab :to="{ name: 'flags' }" label="Flags" />
          <q-route-tab :to="{ name: 'teams' }" label="Teams" />
        </q-tabs>
        <q-space />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <slot />
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "BaseLayout",
};
</script>

<style></style>
