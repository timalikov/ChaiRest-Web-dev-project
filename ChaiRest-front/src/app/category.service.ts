import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Category, Furniture} from './models';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {
  private baseUrl = 'http://localhost:8000/category\n';

  constructor(private http: HttpClient) { }

  getCourses(): Observable<Category[]> {
    return this.http.get<Category[]>(`${this.baseUrl}/`);
  }

  getCategory(id: number): Observable<Category> {
    return this.http.get<Category>(`${this.baseUrl}/${id}/`);
  }

  getFurniture(id: number): Observable<Furniture[]> {
    return this.http.get<Furniture[]>(`${this.baseUrl}/${id}/furniture/`);
  }
}
