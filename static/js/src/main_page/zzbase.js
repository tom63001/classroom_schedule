class search_menu {
    constructor(root) {
        this.root = root;
        this.platform = "Web";
        /* if (this.root.os)
        *  for further multi-end development
        */

        this.$displayed_content = $(`
    <div class="empty"></div>
    <form method="GET" id="post_form" action={% url 'index' %}>  
        <input type="text" id="classroom" list="rooms" name="classroom_to_find" class="input_block" value="Classroom? Instructor?"
               onclick="if(this.value=='Classroom? Instructor?') {this.value='';}"
               onblur="if(this.value=='') {this.value='Classroom? Instructor?'}">

        <div class="empty2"></div>     
        <input type="submit" value="Find Schedule" class="submit_button">
        <div class="empty2"></div>    
    </form>
        `);

        this.root.$classroom_search.append(this.$displayed_content);

        this.$query_button = this.$displayed_content.find('.submit_button');
        this.start();
    }

    get_classroom_info(e) {
        let outer = this;
        $.ajax({
            url: "https://114514.boo/main_page/get_info/",
            type: "GET",
            id: "post_form",
            data: {
                classroom: $("#classroom").val()
            },
            success: function(json) {
                console.log(json);
                this.$existed_table = $('#result');
                if (this.$existed_table)
                    this.$existed_table.remove();
                if (Object.keys(json[0]).length === 4) {
                    this.$classroom_information = "<table id='result' class='classroom_result'> " +
                    "  <tr>" +
                    "    <th>Day</th>\n" +
                    "    <th>Time</th>\n" +
                    "    <th>Scheduled Course</th>\n" +
                    "    <th>Course Title</th>\n" +
                    "  </tr>";
                    for (let value of json) {
                        this.$classroom_information += "<tr>";
                        this.$classroom_information += "<td>" + value["day"] + "</td>"
                        this.$classroom_information += "<td>" + value["time"] + "</td>"
                        this.$classroom_information += "<td>" + value["scheduled course"] + "</td>"
                        this.$classroom_information += "<td>" + value["course title"] + "</td>"
                        this.$classroom_information += "</tr>";
                    }
                    this.$classroom_information += "</table>"
                }
                else if (Object.keys(json[0]).length === 2) {
                    this.$classroom_information = "<table id='result' class='instructor_result'> " +
                    "  <tr>" +
                    "    <th>Scheduled Course</th>\n" +
                    "    <th>Course Title</th>\n" +
                    "  </tr>";
                    for (let value of json) {
                        this.$classroom_information += "<tr>";
                        this.$classroom_information += "<td>" + value["scheduled course"] + "</td>"
                        this.$classroom_information += "<td>" + value["course title"] + "</td>"
                        this.$classroom_information += "</tr>";
                    }
                    this.$classroom_information += "</table>"
                }
                outer.root.$classroom_search.append(this.$classroom_information);
            }
        });
        e.preventDefault();
    }

    start() {
        this.add_listening_event();
        let $auto_fill =

        console.log("prepared to autofill");
        this.root.$datas.append($auto_fill);
    }

    add_listening_event() {
        let outer = this;
        this.$query_button.click(function(e) {
            outer.get_classroom_info(e);
            console.log("query button clicked");
        });
    }
}