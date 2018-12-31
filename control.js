var app = new Vue({
    el: '#todos',
    data: {
        todos: null,
        "todo.done": true
    },
    mounted: function () {
        axios.
            get('https://us-central1-todo-188905.cloudfunctions.net/get').
            then(response => (
                this.todos = response.data
            ))
    },
    methods: {
        finishTodo: function (id) {
            axios.
                get('https://us-central1-todo-188905.cloudfunctions.net/finishTodo').
                then(response => (
                    this.todos = response.data
                ))
        }
    }
})