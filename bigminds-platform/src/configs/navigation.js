import menuPages from './menus/pages.menu'

export default {
  // main navigation - side menu
  menu: [{
    text: '',
    key: '',
    items: [
      { icon: 'mdi-view-dashboard-outline', key: 'Retargeting', text: 'Retargeting', link: '/retargeting' }
    ]
  }],

  // footer links
  footer: [{
    text: 'Code',
    key: 'Código',
    href: 'https://github.com/rodrigoase/bbva-hackaton-bigminds',
    target: '_blank'
  }]
}
