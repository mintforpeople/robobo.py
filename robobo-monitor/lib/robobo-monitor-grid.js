document.addEventListener('DOMContentLoaded', function () {

  //
  // Initialize stuff
  //

  var grid = null;
  var docElem = document.documentElement;
  var monitor = document.querySelector('.monitor');
  var gridElement = monitor.querySelector('.grid');

  var dragOrder = [];
  var uuid = 0;

  //
  // Grid helper functions
  //

  function initDemo() {
    initGrid();

    gridElement.addEventListener('click', function (e) {
        if (elementMatches(e.target, '.card-icon')) {
          item = e.target.parentElement.parentElement.parentElement;
          cardContent = e.target.parentElement.getElementsByClassName('card-content')[0];
          clickExpandCollapse(e.target, cardContent, item);
        }
      });


    function clickExpandCollapse(iconElement, contentElement, item) {
        if (contentElement.classList.contains('card-content-collapsed')) {
           expandCard(iconElement,contentElement);
        }else {
          collapseCard(iconElement, contentElement);
        }
        grid.refreshItems();
        /*
        grid.remove(item);
        grid.add([item]);
        updateIndices();
        */
    }

    function expandCard(iconElement, contentElement) {
      contentElement.classList.remove("card-content-collapsed");
      contentElement.classList.add("card-content-expanded");
    }

    function collapseCard(iconElement, contentElement) {
      contentElement.classList.remove("card-content-expanded");
      contentElement.classList.add("card-content-collapsed");
    }



  }

  function initGrid() {

    var dragCounter = 0;

    grid = new Muuri(gridElement, {
      items: '.item',
      layout: {
        fillGaps: false,
        horizontal: false,
        alignRight: false,
        alignBottom: false,
        rounding: true
      },
      layoutDuration: 400,
      layoutEasing: 'ease',
      dragEnabled: true,
      dragSortInterval: 50,
      dragContainer: document.body,
      dragStartPredicate: {
        handle: '.card-title'
      },
/*
      dragStartPredicate: function (item, event) {
        var isCollapseAction = elementMatches(event.target, '.card-icon, .card-icon i');
        return !isCollapseAction ? Muuri.ItemDrag.defaultStartPredicate(item, event) : false;
      },
      */
      dragReleaseDuration: 400,
      dragReleseEasing: 'ease'
    })
    .on('dragStart', function () {
      ++dragCounter;
      docElem.classList.add('dragging');
    })
    .on('dragEnd', function () {
      if (--dragCounter < 1) {
        docElem.classList.remove('dragging');
      }
    })
    .on('move', updateIndices);
  }


  function updateIndices() {
      grid.getItems().forEach(function (item, i) {
        item.getElement().setAttribute('data-id', i + 1);
      });

  }

  function elementMatches(element, selector) {
    var p = Element.prototype;
    return (p.matches || p.matchesSelector || p.webkitMatchesSelector || p.mozMatchesSelector || p.msMatchesSelector || p.oMatchesSelector).call(element, selector);

  }

  initDemo();

});
