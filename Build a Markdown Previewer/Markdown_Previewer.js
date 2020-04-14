const defaultContent=`# Welcome to my React Markdown Previewer!

  ## This is a sub-heading...
  ### And here's some other cool stuff:
    
  Heres some code, \`<div></div>\`, between 2 backticks.

  \`\`\`
  // this is multi-line code:

  function anotherExample(firstLine, lastLine) {
    if (firstLine == '\`\`\`' && lastLine == '\`\`\`') {
      return multiLineCode;
    }
  }
  \`\`\`
    
  You can also make text **bold**... whoa!
  Or _italic_.
  Or... wait for it... **_both!_**
  And feel free to go crazy ~~crossing stuff out~~.

  There's also [links](https://www.freecodecamp.com), and
   > Block Quotes!

  And if you want to get really crazy, even tables:

  Wild Header | Crazy Header | Another Header?
  ------------ | ------------- | ------------- 
  Your content can | be here, and it | can be here....
  And here. | Okay. | I think we get it.

  - And of course there are lists.
    - Some are bulleted.
        - With different indentation levels.
          - That look like this.


  1. And there are numbererd lists too.
  1. Use just 1s if you want! 
  1. But the list goes on...
  - Even if you use dashes or asterisks.
  * And last but not least, let's not forget embedded images:

  ![React Logo w/ Text](https://goo.gl/Umyytc)
  `;

const body={
    height:"100%",
    width:"100%",
    display:"flex",
    flexWrap:"wrap",
    justifyContent:"center",
};

const editorTitleStyle={
    width:"49%",
    height: "10%",
    border:"1px solid black",
    textAlign:"center",
    fontSize:"2em",

};
const previewTitleStyle={
    width:"49%",
    height: "10%",
    border:"1px solid black",
    textAlign:"center",
    fontSize:"2em",
};


const editorStyle={
    width:"48.8%",
    height: "90",
    border:"1px solid black",
    resize:"none",
    overflowY:"auto",
};


const previewStyle={
    width:"49%",
    height: "90vh",
    border:"1px solid black",
    overflowY:"auto",
};


class MarkViever extends React.Component {
  constructor(props) {
  super(props);
    this.state = {
      input: defaultContent,
    };
    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(event) {
    this.setState({
      input: event.target.value
    })
  }



  render() {
    return (
        <div id="all" style={body}>
            <div style={editorTitleStyle}>Editor</div>
            <div style={previewTitleStyle}>Preview</div>
            <textarea  id="editor"  style={editorStyle} value={this.state.input} onChange={this.handleChange} />
            <div style={previewStyle} id="preview"  dangerouslySetInnerHTML={{__html: marked(this.state.input)}} />
        </div>
    )
  }
}

ReactDOM.render(<MarkViever />, document.getElementById('all'))


/*
<div ><textarea style={editorStyle} id="editor"  value={this.state.input} onChange={this.handleChange} /></div>
<div style={previewStyle}><div  id="preview"  dangerouslySetInnerHTML={{__html: marked(this.state.input)}} /></div>
 */
