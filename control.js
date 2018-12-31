var app = new Vue({
    el: '#todos',
    data: {
        todos: null,
        name: '',
        quantity: ''
    },
    mounted: function () {
        axios.
            get('https://us-central1-todo-188905.cloudfunctions.net/get').
            then(response => (
                this.todos = response.data
            ))
    },
    computed: {
        nameState: function () {
            return this.name.length > 2 ? true : false
        },
        quantityState: function () {
            return this.quantity.length > 0 ? true : false
        }
    },
    methods: {
        finishTodo: function (id) {
            axios.
                post('https://us-central1-todo-188905.cloudfunctions.net/finishTodo', { 'id': id }).
                then(response => (
                    this.todos = response.data
                ))
        },
        addTodo: function (name, quantity) {
            axios.
                post('https://us-central1-todo-188905.cloudfunctions.net/addTodo', { 'name': name, 'quantity': quantity }).
                then(response => (
                    this.todos = response.data
                ))
        }
    }
})