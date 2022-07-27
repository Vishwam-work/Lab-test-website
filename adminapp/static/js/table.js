var $table = $('#table');
    $(function () {
        $('#toolbar').find('select').change(function () {
            $table.bootstrapTable('refreshOptions', {
                exportDataType: $(this).val()
            });
        });
    })

		var trBoldBlue = $("table");

	$(trBoldBlue).on("click", "tr", function (){
			$(this).toggleClass("bold-blue");
	});
    function LinkFormatter(value, row, index) {
        return "<a href='"+row.url+"'>"+value+"</a>";
      }