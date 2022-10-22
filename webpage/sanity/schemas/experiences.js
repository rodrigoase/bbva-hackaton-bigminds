export default{
    name:'experiences',
    title:'Experiences',
    type: 'document',
    fields:[
        {
            name:'title',
            title:'Title',
            type:'string'
        },
        {
            name:'skills',
            title:'Skills',
            type:'array',
            of:[{ type:'skills'}]
        },
    ]
}