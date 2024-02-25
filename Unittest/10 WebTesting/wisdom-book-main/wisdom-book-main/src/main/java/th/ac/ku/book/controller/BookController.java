package th.ac.ku.book.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import th.ac.ku.book.model.Book;
import th.ac.ku.book.service.BookService;

@Controller
@RequestMapping("/book")
public class BookController {

    @Autowired
    private BookService service;

    @GetMapping
    public String getBooks(Model model) {
        model.addAttribute("books", service.getAll());
        return "books";
    }

    @GetMapping("/add")
    public String getAddPage() {
        return "book-add";
    }

    @PostMapping("/add")
    public String addBook(@ModelAttribute Book book, Model model) {
        service.create(book);
        return "redirect:/book";
    }

}
