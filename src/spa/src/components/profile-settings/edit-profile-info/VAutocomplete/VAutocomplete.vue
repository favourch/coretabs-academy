<template>
<div>
  <div tabindex="0" @focusin="hasFocus=true" class="v-autocomplete-select">
    <v-text-field append-icon="arrow_drop_down" v-if="inputValue && !switchInput" :label="form.country" :value="inputValue.text" @focus="switchInput=true"></v-text-field>
    <v-text-field append-icon="arrow_drop_down" v-else :label="form.country" @focus="hasFocus=true" autocomplete="off" ref="search" v-model="search" @keyup="moveToResults" @keydown="removeOption"></v-text-field>
    <v-slide-y-transition>
    <div v-if="showResultList" ref="resultList" class="countries-list">
      <div tabindex="0" ref="result" class="result" v-for="result in results" :key="result[optionValue]" v-html="highlight(result[optionText])" @click="selectOption(result)" @keyup.prevent="navigateResults(result, $event)">
      </div>
    </div>
    </v-slide-y-transition>
  </div>
</div>
</template>

<script>
export default {
  props: {
    placeholder: {
      type: String,
      default: 'search',
      required: false
    },
    options: {
      type: Array,
      default: function() {
        return []
      },
      required: true
    },
    optionValue: {
      type: String,
      default: 'value',
      required: true
    },
    optionText: {
      type: String,
      default: 'text',
      required: true
    },
    inputValue: {
      type: String,
      default: 'text',
      required: true
    },
    value: {
      type: Object,
      default: function() {
        return null
      },
      required: false
    }
  },
  data: function() {
    return {
      hasFocus: false,
      search: null,
      selectedOption: this.value,
      selectedResult: 0,
      switchInput: false
    }
  },
  mounted() {
    window.addEventListener('click', this.loseFocus)
  },
  destroyed() {
    window.removeEventListener('click', this.loseFocus)
  },
  computed: {
    results: function() {
      return this.search ? this.options.filter(i => String(i[this.optionText]).toLowerCase().indexOf(this.search.toLowerCase()) > -1) : this.options
    },
    showResultList: function() {
      return this.hasFocus && this.results.length > 0
    },
    showPlaceholder: function() {
      return !this.hasFocus && !this.selectedOption
    },
    form() { return this.$store.state.i18n.form }
  },
  watch: {
    hasFocus: function(hasFocus) {
      window.removeEventListener('keydown', this.stopScroll)
      if (hasFocus) {
        window.addEventListener('keydown', this.stopScroll)
        this.$refs.search.focus()
      } else {
        this.search = null
        this.selectedResult = 0
        this.$refs.search.blur()
      }
    },
    value: function() {
      this.options.forEach(option => {
        if (this.value && option[this.optionValue] == this.value[this.optionValue]) {
          this.selectedOption = option
        }
      })
    },
    selectedOption: function() {
      this.$emit('input', this.selectedOption)
      console.log(this.selectedOption)
      this.search = this.selectedOption.text
    },
    search: function() {
      this.$emit('search', this.search)
    }
  },
  methods: {
    selectOption: function(option) {
      this.selectedOption = option
      this.hasFocus = false
    },
    removeOption: function(event) {
      if (event.keyCode === 8 && (this.search === null || this.search === '')) {
        this.selectedOption = null
        this.hasFocus = false
      }
    },
    moveToResults: function(event) {
      if (event.keyCode === 40) {
        if (this.$refs.result.length > 0) {
          this.$refs.resultList.children.item(0).focus()
        }
      }
    },
    navigateResults: function(option, event) {
      if (event.keyCode === 13) {
        this.selectOption(option)
      } else if (event.keyCode === 40 || event.keyCode === 38) {
        if (event.keyCode === 40) {
          this.selectedResult++
        } else if (event.keyCode === 38) {
          this.selectedResult--
        }
        let next = this.$refs.resultList.children.item(this.selectedResult)
        if (next) {
          next.focus()
        } else {
          this.selectedResult = 0
          this.$refs.search.focus()
        }
      }
    },
    highlight: function(value) {
      if (this.search) {
        let matchPos = String(value).toLowerCase().indexOf(this.search.toLowerCase())
        if (matchPos > -1) {
          let matchStr = String(value).substr(matchPos, this.search.length)
          value = String(value).replace(matchStr, '<span style="font-weight: bold; background-color: #efefef;">' + matchStr + '</span>')
        }
      }
      return value
    },
    stopScroll: function(event) {
      if (event.keyCode === 40 || event.keyCode === 38) {
        event.preventDefault()
      }
    },
    loseFocus: function(event) {
      if (!this.$el.contains(event.target)) {
        this.hasFocus = false
        this.switchInput = false
      }
    }
  }
}
</script>

<style scoped>
.v-autocomplete-select {
  position: relative;
  cursor: text;
  display: block;
}

.v-autocomplete-select i.dropdown {
  width: 0;
  height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 4px solid;
  float: right;
  top: .75em;
  opacity: .8;
  cursor: pointer;
}

.v-autocomplete-select .placeholder {
  display: inline-block;
  color: #ccc;
}

.v-autocomplete-select .countries-list {
  width: calc(100% + 2px);
  min-width: calc(100% + 2px);
  cursor: pointer;
  position: absolute;
  top: 55px;
  max-height: 300px !important;
  overflow-y: scroll;
  z-index: 10;
  background-color: #fff;
  box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.2), 0 8px 10px 1px rgba(0, 0, 0, 0.14), 0 3px 14px 2px rgba(0, 0, 0, 0.12);
  -webkit-box-shadow: 0 5px 5px -3px rgba(0, 0, 0, 0.2), 0 8px 10px 1px rgba(0, 0, 0, 0.14), 0 3px 14px 2px rgba(0, 0, 0, 0.12);
}

.v-autocomplete-select .countries-list .result {
  padding: 1em .75em;
  color: #333;
}

.v-autocomplete-select .countries-list .result:hover,
.v-autocomplete-select .countries-list .result:focus {
  background-color: #efefef;
  outline: none;
}

.v-autocomplete-select .selected-option {
  display: inline-block;
}

.v-autocomplete-select .search {
  border: none;
  width: 50px;
}

.v-autocomplete-select .search:focus {
  outline: none;
}
</style>
