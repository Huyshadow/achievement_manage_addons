odoo.define(
  "web_list_view_general_buttons.Check_Button_Appear",
  function (require) {
    "use strict";
    var rpc = require("web.rpc");
    // Function to get the field value
    function getFieldFromModel() {
      var model = "achievement.user.list"; // Replace with your actual model name
      var field = "user_approve"; // Replace with your actual field name
      var recordId = 1; // Replace with the ID of the record you want to retrieve the field value from

      rpc
        .query({
          model: model,
          method: "read",
          args: [recordId, [field]],
        })
        .then(function (result) {
          var fieldValue = result[0].user_approve;
          if (fieldValue === true) {
            console.log(
              $(
                "button.btn.btn-secondary.btn-custom.o_discard_button"
              ).addClass("hidden")
            );
          }
          // Do something with the field value
        });
    }
    // Call the function to get the field value
    getFieldFromModel();
  }
);
