call plug#begin('~/.vim/plugged')

Plug 'vim-airline/vim-airline'
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }
Plug 'luochen1990/rainbow'
“Plug 'Valloric/YouCompleteMe'

call plug#end()

"vim-go插件快捷键
au FileType go nmap <C-d> <Plug>(go-def-vertical)
au FileType go nmap <C-f> <Plug>(go-implements)
"au FileType go nmap <C-f> :GoImplements <cr>
au FileType go nmap <C-e> :GoReferrers <cr>


"启动括号颜色
let g:rainbow_active = 1


"=======================

"语法高亮
syntax on
filetype on

set expandtab
set ts=4
set shiftwidth=4
set ignorecase

set hlsearch  "搜索高亮
set ruler
set scrolloff=5  "上下5行
set wildmenu   "vs不全
set wildmode=longest:list,full
set nocompatible  "不兼容历史

command WQ wq
command Wq wq
command Vs vs
command W w
command Q q

" 记录文件打开位置
set viminfo='10,\"100,:20,%,n~/.viminfo 
au BufReadPost * if line("'\"") > 0|if line("'\"") <= line("$")|exe("norm '\"")|else|exe "norm $"|endif|endif


"关闭缩进
set nosmartindent
set noautoindent
filetype indent off

“set backspace=2 " 解决插入模式下delete/backspce键失效问题
”set completeopt-=preview "关闭YCM顶部预览
