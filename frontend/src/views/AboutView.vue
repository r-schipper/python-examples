<template>
  <div>{{ answer }}</div>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      answer: {},
    };
  },
  methods: {
    async getAnswer() {
      // const { data } = await axios.get("https://yesno.wtf/api");
      const { data } = await axios.get("http://127.0.0.1:5000/test-api");
      this.answer = data;
    },
  },
  beforeMount() {
    this.getAnswer();
  },
};
</script>