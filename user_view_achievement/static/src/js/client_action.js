odoo.define('user_view_achievement.Achievement', function (require) {
    'use strict';
    
    var AbstractAction = require('web.AbstractAction')
    var core = require('web.core')
    var QWeb = core.qweb;
    
    var AchievementAction = AbstractAction.extend({
        contentTemplate: 'achievement_detail',
        hasControlPanel: true,
        // events: _.extend({}, AbstractAction.prototype.events, {
            
        // }),

        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.action = action;
            this.context = action.context;
            this.name = false; 
            this.status = "";
        },

        async willStart(){
            await this._super(...arguments);
            await this._getRecordId();
        },

        start: async function(){
            await this._super(...arguments);
            await this._renderRecord();
        },

        _getRecordId: function() {
            var self = this;
            return this._rpc({
                model: 'create_achievement.achievement',
                method: 'get_name',
                args: [parseInt(this.context.active_id)]
            }).then(function(resultData){
                self.name = resultData.name;
                self.status = resultData.status
            })
        },
        
        _renderRecord: async function () {
            this.$el.find('.render_name').append($(QWeb.render('achievement_name', {
                o: this,
            })));
        }

    });

    core.action_registry.add('achievement_detail', AchievementAction);
    
    return AchievementAction;
    
});
