// odoo.define('res.user', function (require) {
//     'use strict';
    
//     var AbstractAction = require('web.AbstractAction')
//     var core = require('web.core')
//     var QWeb = core.qweb;
    
//     var UserAction = AbstractAction.extend({
//         contentTemplate: 'profile_detail',
//         hasControlPanel: true,
//         // events: _.extend({}, AbstractAction.prototype.events, {
            
//         // }),

//         init: function (parent, action) {
//             this._super.apply(this, arguments);
//             this.action = action;
//             this.context = action.context;
//             this.name = false; 
//             this.status = "";
//         },

//         async willStart(){
//             await this._super(...arguments);
//             await this._getRecordId();
//         },

//         start: async function(){
//             await this._super(...arguments);
//             await this._renderRecord();
//         },

//         _getRecordId: function() {
//             var self = this;
//             return this._rpc({
//                 model: 'create_achievement.achievement',
//                 method: 'get_profile',
//                 args: [parseInt(this.context.active_id)]
//             }).then(function(resultData){
//                 self.name = resultData.name;
//                 self.mssv_mscb = resultData.mssv_mscb;
//                 self.email_canhan = resultData.email_canhan;
//             })
//         },
        
//         _renderRecord: async function () {
//             this.$el.find('.render_name').append($(QWeb.render('user_name', {
//                 o: this,
//             })));
//         }

//     });

//     core.action_registry.add('user_detail', UserAction);
    
//     return UserAction;
    
// });
