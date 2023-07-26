console.log('hellow')
const delContainer = document.querySelector('.container')
delContainer.addEventListener('click', (e)=>{
    if(e.target.closest('.notification')) e.target.closest('.notification').remove()
})