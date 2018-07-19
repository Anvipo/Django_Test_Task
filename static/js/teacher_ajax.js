$(document).ready(function () {
    //TODO почему-то срабатывает только 1 раз
    $(".deleteTeacherBtn").click(delete_teacher);

    function redrawTable(data) {
        const table_teacher = document.getElementById("id_teachers");

        let new_table_value = '';
        data = JSON.parse(data);
        data.forEach(function (element) {
            new_table_value += '<tr>\n';
            const list = element.split(' ');
            new_table_value += '\t<td>' + list[0] + '</td>\n';
            new_table_value += '\t<td>' + list[1] + '</td>\n';
            new_table_value += '\t<td>' + list[2] + '</td>\n';

            new_table_value += '<td>\n' +
                '<button type="button" value="' + list[3] + '" class="btn btn-danger deleteTeacherBtn"' +
                ' id="id_delete_teacher">\n' +
                '\tУдалить\n' +
                '</button>\n' +
                '</td>';
            new_table_value += '<tr>\n';
        });

        table_teacher.innerHTML = new_table_value;

    }

    function delete_teacher() {
        const id_deleted_teacher = $(this).val();

        $.ajax({
            type: "GET",
            url: "/teachers/ajax/",
            data: {'delete_data': id_deleted_teacher},
            cache: false,
            success: function (data) {
                redrawTable(data)
            }
        })
    }

    $("#id_add_teacher").click(add_teacher);

    function add_teacher() {
        const teacher_last_name = $("#id_last_name").val();
        const teacher_first_name = $("#id_first_name").val();
        const teacher_patronymic = $("#id_patronymic").val();

        $.ajax({
            type: "GET",
            url: "/teachers/ajax/",
            data: {
                'teacher_last_name': teacher_last_name,
                'teacher_first_name': teacher_first_name,
                'teacher_patronymic': teacher_patronymic,
            },
            cache: false,
            success: function (data) {
                redrawTable(data)
            }
        })
    }
});
