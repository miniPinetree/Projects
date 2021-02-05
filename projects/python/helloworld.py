function get_members(){
    return ['egoing', 'k8805', 'gomi']
}
members = get_members()

for(i=0
    i < members.length
    i++){
    document.write(members[i].toUpperCase())
    document.write('<br/>')
}
