const title = 'Quotes App';

const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
  }

const typeWriter = async () => {
        for(let i=0; i < title.length; i++) {
            await sleep(200);
            document.getElementById('headline-title').innerHTML += title.charAt(i);
            
        }
        
}

typeWriter();