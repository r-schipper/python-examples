
<template>
  <div>
    <p>Message is: {{ message }}</p>
    <input v-model="message" placeholder="edit me" /> <button @click="send">send</button>
    <div>{{ answer }}</div>
    
    <p>Date in the past: {{ date_in_the_past }}</p>
    <input v-model="date_in_the_past" placeholder="edit me" /> <button @click="get_days_ago">get days ago</button>
    <div>{{ days_ago }}</div>
  </div>

  
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      answer: {},
      message: "",
      date_in_the_past: "2021-01-01",
      days_ago: "",

    };
  },
  methods: {
    async getAnswer() {
      // const { data } = await axios.get("https://yesno.wtf/api");
      const { data } = await axios.get("http://127.0.0.1:5000/test-api");
      this.answer = data;
    },
    async send(event) {
      console.dir(this.message)
      const { data } = await axios.get("http://127.0.0.1:5000/test-api?name="+this.message);
      this.answer = data;
    },
    async get_days_ago(event) {
      const { data } = await axios.get("http://127.0.0.1:5000/days-ago?date_in_the_past="+this.date_in_the_past);
      console.dir(data);
      this.days_ago = data.data.daysAgo;
    },
  },
  beforeMount() {
    this.getAnswer();
  },
};
</script>