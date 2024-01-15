export class cr_search {
    constructor(id, os) {
        this.id = id;
        this.os = os;
        this.$classroom_search = $('#' + id);
        this.menu = new search_menu(this);
        this.$datas = $('#rooms');
        console.log(this.$datas);
    }
}
