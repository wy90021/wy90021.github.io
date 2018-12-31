var app = new Vue({
    el: '#todos',
    data: {
        todos: null,
        pageStartup: false
    },
    mounted: function () {
        axios.
            get('https://us-central1-todo-188905.cloudfunctions.net/get').
            then(response => (
                this.todos = response.data,
                this.pageStartup = true
            ))
    },
    methods: {
        finishTodo: function (id) {
            axios.
                post('https://us-central1-todo-188905.cloudfunctions.net/finishTodo', { 'id': id }).
                then(response => (
                    this.todos = response.data
                ))
        }
    }
})