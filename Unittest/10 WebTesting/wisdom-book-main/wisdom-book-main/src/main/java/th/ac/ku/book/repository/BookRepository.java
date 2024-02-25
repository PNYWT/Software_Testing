package th.ac.ku.book.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import th.ac.ku.book.model.Book;

@Repository
public interface BookRepository extends JpaRepository<Book, Integer> {
}
