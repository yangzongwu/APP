const bodyStyle={
    backgroundColor:"gainsboro",
    width: "100%",
    height:"100%",
    position:"absolute",
    top:"0px",
    bottom:"0px",
    left:"0",
    right:"0",
    textAlign:"center"
};
const BoxStyles={
    backgroundColor: "white",
    fontSize:"2em",
    margin:"auto",
    width:"600px",
    marginTop:"15%",
};
const quoteStyles ={
    backgroundColor: "white",
    color:"blue",
    paddingRight:  '1em',
    paddingLeft:"10px",
    paddingTop:"10px",
    textAlign:"center",
};

const nameStyles={
    backgroundColor: "white",
    color:"red",
    fontSize: '1em',
    marginRight:"20px",
    textAlign:"right",
    paddingRight:"20px",
};

const buttonsStyles={
    textAlign:"right",
    marginBottom:"10px",
};

const buttonStyles={
    marginRight:"10px",
    fontSize: '0.5em',
    marginBottom: "10px",
};

const twitterStyles={
    marginLeft:"20px",
    float:"left",
    fontSize: '0.5em',
    paddingTop:"15px",
};


class QuoteComponent extends React.Component {
    constructor(pros){
        super(pros);
        this.state={
            quote:"Happiness is not something readymade. It comes from your own actions.",
            author:"- Dalai Lama",
            color:"red",
            colorPicker:["red","blue","yellow","gray","green","SILVER","BLACK","MAROON","OLIVE"],
            quotePicker:[
                ["Fall seven times and stand up eight.","- Japanese Proverb"],
                ["I have learned over the years that when one’s mind is made up, this diminishes fear.","- Rosa Parks"],
                ["Teach thy tongue to say, “I do not know,” and thous shalt progress.","- Maimonides"],
            ]
        };
        this.handleClick=this.handleClick.bind(this);
    }

    handleClick(){
        let temp=this.state.quotePicker[Math.floor(Math.random()*this.state.quotePicker.length)];
        let curcolor='#' + (function co(lor){   return (lor +=
  [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'][Math.floor(Math.random()*16)])
  && (lor.length === 6) ?  lor : co(lor); })('');
        this.setState({
            quote:temp[0],
            author:temp[1],
            color:curcolor,
        })
    }
    render(){
        let curColor=this.state.color;
        let curQuote=this.state.quote;
        let curAuthor=this.state.author;

        return(
            <div style={bodyStyle}>
                <div style={{backgroundColor:curColor,width: "100%", height:"100%", position:"absolute",}}>
                <div id="quote-box" style={BoxStyles}>

                    <div id="text" style={quoteStyles}>
                        <p style={{color:curColor}}>{curQuote}</p>
                    </div>
                    <div id="author" style={nameStyles}>
                        <p style={{color:curColor}}>{curAuthor}</p>
                    </div>
                    <div id="button" style={buttonsStyles}>
                        <a id="tweet-quote"  style={twitterStyles} href={"https://twitter.com/intent/tweet?hashtags=quotes&related"} target="_blank">Twitter</a>
                        <button id="new-quote" style={buttonStyles} onClick={this.handleClick}>New Quote</button>
                    </div>
                </div>
            </div>
            </div>
        )
    }

}


ReactDOM.render(<QuoteComponent />, document.getElementById("all"));
