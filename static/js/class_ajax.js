$(document).ready(function () {
    //TODO почему-то срабатывает только 1 раз
    $(".deleteClassBtn").click(delete_class);

    function delete_class() {
        const id_deleted_class = $(this).val();
        $.ajax({
            type: "GET",
            url: "/classes/ajax/",
            data: {'delete_data': id_deleted_class},
            cache: false,
            success: function (data) {
                redrawTable(data)
            }
        })
    }

    function redrawTable(data) {
        const classes_table = document.getElementById("id_classes");

        let new_table_value = '';
        data = JSON.parse(data);
        data.forEach(function (element) {
            new_table_value += '<tr>\n';
            const list = element.split(', ');
            new_table_value += '\t<td>' + list[0] + '</td>\n';
            new_table_value += '\t<td>' + list[1] + '</td>\n';
            new_table_value += '\t<td>' + list[2] + '</td>\n';

            new_table_value += '<td>\n' +
                '<button type="button" value="' + list[0] + '" class="btn btn-danger deleteClassBtn"' +
                ' id="id_delete_class">\n' +
                '\tУдалить\n' +
                '</button>\n' +
                '</td>';
            new_table_value += '<tr>\n';
        });

        classes_table.innerHTML = new_table_value;

    }

    $("#id_add_class").click(add_class);

    function add_class() {
        const class_title = $("#id_title").val();
        const class_description = $("#id_description").val();
        const class_teacher = $("#id_teacher").val();
        $.ajax({
            type: "GET",
            url: "/classes/ajax/",
            data: {
                'class_title': class_title,
                'class_description': class_description,
                'class_teacher': class_teacher,
            },
            cache: false,
            success: function (data) {
                redrawTable(data, 'deleteClassBtn', 'id_delete_class')
            }
        })
    }
});
