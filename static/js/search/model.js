// Generated by CoffeeScript 1.3.3
(function() {
  var __hasProp = {}.hasOwnProperty,
    __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

  mtracker.search.model.HitGroupContentSearch = (function(_super) {

    __extends(HitGroupContentSearch, _super);

    function HitGroupContentSearch() {
      return HitGroupContentSearch.__super__.constructor.apply(this, arguments);
    }

    HitGroupContentSearch.prototype.urlRoot = '/api/hitgroupcontentsearch/';

    return HitGroupContentSearch;

  })(crud.model.Model);

  mtracker.search.model.HitGroupContentSearch = (function(_super) {

    __extends(HitGroupContentSearch, _super);

    function HitGroupContentSearch() {
      return HitGroupContentSearch.__super__.constructor.apply(this, arguments);
    }

    HitGroupContentSearch.prototype.model = mtracker.search.model.HitGroupContentSearch;

    HitGroupContentSearch.prototype.urlRoot = '/api/hitgroupcontentsearch/';

    HitGroupContentSearch.prototype.multi_field_ordering = true;

    return HitGroupContentSearch;

  })(crud.collection.Collection);

}).call(this);
