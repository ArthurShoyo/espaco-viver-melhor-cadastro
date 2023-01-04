var header = document.getElementById('header');
var navigationHeader = document.getElementById("navigation_header");
var content = document.getElementById('content');
var showSidebar = false;

function toggleSidebar()
{
    showSidebar = !showSidebar;
    if(showSidebar)
    {
         navigationHeader.style.marginLeft = '-10vw';
         navigationHeader.style.animationName = 'showSidebar'
         content.style.filter = 'blur(2px)';
         
    }
    else
    {
        navigationHeader.style.marginLeft = '-100vw';
        navigationHeader.style.animationName = '';
        content.style.filter = '';
    }
}

function closeSidebar()
{
    if(showSidebar)
    {
        toggleSidebar();
    }
}

window.addEventListener('resize', function(event){
    if(window.innerWidth > 768 && showSidebar)
    {
        toggleSidebar();
    }
})

function btnLink()
{
    window.location.href = "http://127.0.0.1:8000/painel"
}

function excluirconfirm() {
    let accepted = confirm("Voce tem certeza que deseja deletar?");
    if (accepted) {
        document.getElementById('deletar').submit();
    }
    else {
        
        return false
    }

}
textArea = new JTextArea(10, 20)