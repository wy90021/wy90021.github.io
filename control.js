var app = new Vue({
    el: '#todos',
    data() {
        return {
            todos: null,
            "todo.done": true
        }
    },
    mounted() {
        axios.
            get('https://us-central1-todo-188905.cloudfunctions.net/get').
            then(response => (
                this.todos = response.data
            ))
    }
})