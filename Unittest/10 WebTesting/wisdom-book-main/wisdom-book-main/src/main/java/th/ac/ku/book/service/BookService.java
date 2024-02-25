package th.ac.ku.book.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import th.ac.ku.book.model.Book;
import th.ac.ku.book.repository.BookRepository;

import java.util.List;

@Service
public class BookService {

    @Autowired
    private BookRepository repository;

    public List<Book> getAll() {
        return repository.findAll();
    }

    public Book create(Book book) {
        repository.save(book);
        return book;
    }

    public Book getRestaurant(int id) {
        return repository.findById(id).get();
    }
}
