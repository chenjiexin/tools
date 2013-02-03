if has("syntax")
	syntax on
endif

set tabstop=4
" set softtabstop=4
" 空格缩进
set shiftwidth=4
set autoindent
set smartindent
set cindent
" C/C++缩进方式
"set cinoptions={0,1s,t0,n-2,p2s,(03s,=.5s,>1s,=1s,:1s
set nu
set hlsearch
set showmatch
"set paste
"auto chage dir
set autochdir
"即输即显
set incsearch

set mousemodel=popup
set mouse=a

set guioptions-=T "remove toolbar"
set guioptions-=l
set guioptions-=r
set guioptions-=b

colorscheme desert

let g:session_autosave='yes'

filetype on
filetype plugin on
filetype indent on
"set expandtab
set syn=auto
"show file name only
set guitablabel=%t

" set foldmethod=syntax

" 突出显示当前行
" set cursorline
"
set fencs=utf-8,gb2132,gb18030,ucs-bom,utf-16,gbk,latin1
" let Tlist_Auto_Open = 1

set ignorecase

set makeprg=smake

noremap <F7> :make -j4<CR>
imap <F7> <ESC>:make -j4<CR>
vmap <F7> <ESC>:make -j4<CR>

noremap <F4> <ESC>:copen<CR>
