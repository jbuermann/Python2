<template>
  <div class="table" :class="size">
      <div class="table__header">
          <div class="table__item fieldName">
              <input class="searchBox" type="text" v-model="search" placeholder="Name" />
              <img @click="sortKey=0" class="sortIcon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGvSURBVGhD7ZqxTsMwEIaDkBhYWFhAok2KhAQjI2LnAXgBnoA34A2YaBMpfQGkruydOzOCmNgYgDrtwEK4P7pDqFhIUeMmOfxJv5Q49v3nSLUdu4HH46mXKDHnEN+2kzCZnYWx+ShE11zcLnoDcxrFZh4lWV6IrlHGj9tBpz87DuPs/bsTLJThGVdrNt3YHIZJ9rLYCRGeoQ5Xbyadm7coTMyzrQM/hTqoy82axV5/vktv+9GWuE2oizbcvBkcpGab3vK9LeG/hDZoy2HqpZe+blFSk8UkS2iCGByuHnbSfJMmu7EluZIyY8TisKvlaJRv0HB6Z0+svBALMTn8ihjl6zTB3doSWkoUE7HZxTF5vkamw19JVKchPNjNHbRuuraYVyp4sJ0baLi8shm7ELzYtlpoAru0GboUPNm+GrqD6QX9ED9tZk5FnvDmNJZjP56e0ND4EMXZUx2CN3LgdDwej+e/oGr4VTEhCiqWKIKKRaOgYhlfoOXDqkDFpy6jY/OBUbEdJKjYoBNUbJkKKjaxBRXHCoKKgx5BxdGboOIwVFBxPC3gzwIQ33o8nloIgi9ML52fZvQJ8AAAAABJRU5ErkJggg==">
          </div>
          <div class="table__item fieldAgeRange">Age Range <img @click="sortKey=1" class="sortIcon" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGvSURBVGhD7ZqxTsMwEIaDkBhYWFhAok2KhAQjI2LnAXgBnoA34A2YaBMpfQGkruydOzOCmNgYgDrtwEK4P7pDqFhIUeMmOfxJv5Q49v3nSLUdu4HH46mXKDHnEN+2kzCZnYWx+ShE11zcLnoDcxrFZh4lWV6IrlHGj9tBpz87DuPs/bsTLJThGVdrNt3YHIZJ9rLYCRGeoQ5Xbyadm7coTMyzrQM/hTqoy82axV5/vktv+9GWuE2oizbcvBkcpGab3vK9LeG/hDZoy2HqpZe+blFSk8UkS2iCGByuHnbSfJMmu7EluZIyY8TisKvlaJRv0HB6Z0+svBALMTn8ihjl6zTB3doSWkoUE7HZxTF5vkamw19JVKchPNjNHbRuuraYVyp4sJ0baLi8shm7ELzYtlpoAru0GboUPNm+GrqD6QX9ED9tZk5FnvDmNJZjP56e0ND4EMXZUx2CN3LgdDwej+e/oGr4VTEhCiqWKIKKRaOgYhlfoOXDqkDFpy6jY/OBUbEdJKjYoBNUbJkKKjaxBRXHCoKKgx5BxdGboOIwVFBxPC3gzwIQ33o8nloIgi9ML52fZvQJ8AAAAABJRU5ErkJggg==">
          </div>
          <div v-if="size=='full'" class="table__item fieldDuration">Duration</div>
          <div v-if="size=='full'" class="table__item fieldPlayers"># of Players</div>
      </div>
      <div class="table__body">
          <div class="table__navigation">
            <span  @click="prevPage"> << </span>
            <span> Showing {{paginationStart+1}}-{{paginationEnd+1}} of {{filteredByName.length + 1}}</span>
            <span @click="nextPage"> >> </span>
          </div>

          <div class="table__row" v-for="(items,index) in filteredByName.slice(paginationStart,paginationEnd)">
              <div class="table__item" :class="{
                  fieldName: index==0,
                  fieldAgeRange: index==1,
                  fieldDuration: index==2,
                  fieldPlayers: index==3
                  }"
                  v-for="(item,index) in items"
                  v-if="size=='full' || (size=='mini' && index < 2)"
              >{{ item }}</div>
          </div>

          <div class="table__navigation">
            <span  @click="prevPage"> << </span>
            <span> Showing {{paginationStart+1}}-{{paginationEnd+1}} of {{filteredByName.length + 1}}</span>
            <span @click="nextPage"> >> </span>
          </div>
      </div>
    </div>
</template>

<script>
  import {games} from './assets/game'

  export  default {
    name: 'gamesTable',
    props: {
      size:{
        type: String,
        default: 'full',
        validator: value => {return (value === 'mini' || value === 'full')}
      }
    },
    data: function () {
        return {
            gameData:games,
            search:"",
            sortKey: 0,
            paginationStart:0,
            paginationEnd: 19,
            increment: 20
        }
    },
    methods:
    {
        prevPage:function ()
        {
          let paginationMax = this.filteredByName.length
              this.paginationStart = this.paginationStart - this.increment
              this.paginationEnd   = this.paginationEnd - this.increment

            if(this.paginationStart < 0)
                this.paginationStart = 0

            if(this.paginationEnd < (this.increment-1))
                this.paginationEnd = (this.increment-1)

        },
        nextPage:function()
        {
            let paginationMax = this.filteredByName.length

            this.paginationStart = this.paginationStart + this.increment
            this.paginationEnd   = this.paginationEnd + this.increment

            if(this.paginationStart > (paginationMax - (this.increment-1)))
                this.paginationStart = (paginationMax - (this.increment-1))

            if(this.paginationEnd > paginationMax)
                this.paginationEnd = paginationMax
        }
    },
    computed:
    {
        filteredByName:function()
        {
            let self=this,
                sort=this.sortKey;

            if(sort == 1)
                return this.gameData.filter((game) => game[0].toLowerCase().indexOf(self.search.toLowerCase())>=0).sort(function(a,b){return a[sort]-b[sort]});
            else
                return this.gameData.filter((game) => game[0].toLowerCase().indexOf(self.search.toLowerCase())>=0).sort()
        }
    }
  }
</script>

<style scoped lang="stylus">
.mini.table
  width 350px


.table
  display flex
  flex-flow column
  background-color #2a2a2a
  input
    background-color #444
    padding 5px
    border 1px solid #bebcbc
    &::placeholder
      color white

.table__header
  display flex
  flex-flow row
  font-weight bold
  .table__item
    display flex
    align-items center
    justify-content center
    border none
    &:first-child
      justify-content left
  img
      &.sortIcon
        width 15px
        margin-left 10px
.table__navigation
  display flex
  flex-flow row
  justify-content center
  color white
  padding 10px
  background-color rgba(0,0,0,0.125)
  span
    padding 0 10px
    &:first-child
    &:last-child
      cursor pointer
.table__body
  display flex
  flex-flow column

.table__row
  display flex
  flex-flow row
  &:hover
    background-color rgba(0,0,0,.125)

.table__item
  flex 1
  text-align center
  padding 10px
  border-bottom 1px solid rgba(0,0,0,.125)
  color white
  &:first-child
    flex 2
    text-align left

@media screen and (max-width: 600px)
  .table
     .fieldDuration,
     .fieldPlayers
        display none
      input
        width 98%
</style>
