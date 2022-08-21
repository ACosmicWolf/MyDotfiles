call plug#begin()
Plug 'tpope/vim-sensible'
Plug 'sheerun/vim-polyglot'
Plug 'ghifarit53/tokyonight-vim'
Plug 'catppuccin/nvim', {'as': 'catppuccin'}
Plug 'Yggdroot/indentLine'
Plug 'psliwka/vim-smoothie'
Plug 'mbbill/undotree'
Plug 'tpope/vim-commentary'
Plug 'preservim/nerdtree', { 'on': 'NERDTreeToggle' }
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
Plug 'ryanoasis/vim-devicons'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'tyru/open-browser.vim' " opens url in browser
Plug 'https://github.com/ap/vim-css-color' " CSS Color Preview
Plug 'nvim-lualine/lualine.nvim'
" If you want to have icons in your statusline choose one of these
Plug 'kyazdani42/nvim-web-devicons'

call plug#end()


" Colorscheme
let g:catppuccin_flavour = "macchiato" " latte, frappe, macchiato, mocha

lua << EOF
require("catppuccin").setup()
EOF

colorscheme catppuccin

" Colorscheme end


" Nerd Tree
nnoremap <C-e> :NERDTreeToggle<CR>

" numbers 
set relativenumber 

" lualine
lua << END
require('lualine').setup()
END

" settings
set splitbelow
set splitright

" Cpp stuff

nnoremap <C-c> <Cmd>40vsp input.in<CR>
autocmd filetype cpp nnoremap <F4> :w <bar> exec '!g++ '.shellescape('%').' -o '.shellescape('%:r').' && ./'.shellescape('%:r') '< input.in'<CR>
