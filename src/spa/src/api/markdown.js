/* eslint-disable */
import showdown from 'showdown'

showdown.setFlavor('github')
const markdown = new showdown.Converter({
   emoji: false,
   tables: true,
   underline: true,
   tasklists: true,
   noHeaderId: true,
   strikethrough: true,
   tablesHeaderId: true,
   parseImgDimensions: true
   // splitAdjacentBlockquotes:true,
   // omitExtraWLInCodeBlocks: true,
})


const MarkdownAPI = {
   render(mdText) {
      // return '<iframe width="1000" height="500" src="https://scrimba.com/c/cPvE3cE"></iframe>'
      let youtube = /(?:http?s?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)\/(?:watch\?v=)?(.+)/g
      mdText = mdText.replace(youtube, '<iframe class="youtube" src="https://www.youtube.com/embed/$1" frameborder="0" allowfullscreen></iframe>')
      let html = markdown.makeHtml(mdText)
      html = html.replace(/<blockquote>(.*?)<\/blockquote>/gs, '<blockquote><div class="quotes no-select"><i class="material-icons">format_quote</i></div>$1<div class="quotes no-select"><i class="material-icons">format_quote</i></div></blockquote>')
      html = html.replace(/<pre>(.*?)<\/pre>/gs, '<pre><div class="code-action"><v-btn flat icon><v-icon>content_copy</v-icon></v-btn></div>$1</pre>')
      return html
   }
}

export default MarkdownAPI
