function wireGamesTable()
{
    new Vue({
        el: '#gamesTableApp',
        delimiters: ['${', '}'],
        template: '#gamesTable',
        data: function () {
            return {
                gameData:games,
                search:"",
                sortKey: 0,
                paginationStart:0,
                paginationEnd: 9
            }
        },
        methods:
        {
            prevPage:function () {
              var paginationMax = this.filteredByName.length
                this.paginationStart = this.paginationStart - 10
                this.paginationEnd   = this.paginationEnd - 10



                if(this.paginationStart < 0)
                    this.paginationStart = 0

                if(this.paginationEnd < 9)
                    this.paginationEnd = 9

            },
            nextPage:function(){
                var paginationMax = this.filteredByName.length

                this.paginationStart = this.paginationStart + 10
                this.paginationEnd   = this.paginationEnd + 10

                if(this.paginationStart > (paginationMax - 9))
                    this.paginationStart = (paginationMax - 9)

                if(this.paginationEnd > paginationMax)
                    this.paginationEnd = paginationMax

            }
        },
        computed:
        {
            filteredByName:function()
            {
                var self=this,
                    sort=this.sortKey;


                if(sort == 1)
                {
                    return this.gameData.filter(
                    function(game){
                        return game[0].toLowerCase().indexOf(self.search.toLowerCase())>=0;
                    }).sort(function(a,b){
                        return a[sort]-b[sort]
                    });
                }else{
                    return this.gameData.filter(
                    function(game){
                        return game[0].toLowerCase().indexOf(self.search.toLowerCase())>=0;
                    }).sort();
                }
            }
        },
        created: function(){ }
    })
}